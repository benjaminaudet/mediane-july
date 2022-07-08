"""Example integrating `tkinter`'s `mainloop` with `asyncio`."""
import asyncio
import tkinter as tk
from typing import Any, Awaitable, TypeVar
from random import randrange
T = TypeVar("T")


class AsyncTk(tk.Tk):
    """
    A Tk class that can run asyncio awaitables alongside the tkinter application.

    Use `root.run_with_mainloop(awaitable)` instead of `root.mainloop()` as a way to run
    coroutines alongside it. It functions similarly to using `asyncio.run(awaitable)`.

    Alternatively use `await root.async_loop()` if you need to run this in an asynchronous
    context. Because this doesn't run `root.mainloop()` directly, it may not behave exactly
    the same as using `root.run_with_mainloop(awaitable)`.
    """
    is_running: bool

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.is_running = True

    def __advance_loop(self, loop: asyncio.AbstractEventLoop, timeout, /) -> None:
        """Helper method for advancing the asyncio event loop."""
        # Stop soon i.e. only advance the event loop a little bit.
        loop.call_soon(loop.stop)
        loop.run_forever()
        # If tkinter is still running, repeat this method.
        if self.is_running:
            self.after(timeout, self.__advance_loop, loop, timeout)

    async def async_loop(self, /) -> None:
        """
        An asynchronous variant of `root.mainloop()`.

        Because this doesn't run `root.mainloop()` directly, it may not behave exactly
        the same as using `root.run_with_mainloop(awaitable)`.
        """
        # For threading.
        self.tk.willdispatch()
        # Run initial update.
        self.update()
        # Run until `self.destroy()` is called.
        while self.is_running:
            # Let other code run.
            # Uses a non-zero sleep time because tkinter should be expected to be slow.
            # This decreases the busy wait time.
            await asyncio.sleep(tk._tkinter.getbusywaitinterval() / 10_000)
            # Run one event.
            self.tk.dooneevent(tk._tkinter.DONT_WAIT)

    def run_with_mainloop(self, awaitable: Awaitable[T], /, *, timeout: float = 0.001) -> T:
        """
        Run an awaitable alongside the tkinter application.

        Similar to using `asyncio.run(awaitable)`.

        Use `root.run_with_mainloop(awaitable, timeout=...)` to
        customize the frequency the asyncio event loop is updated.
        """
        if not isinstance(awaitable, Awaitable):
            raise TypeError(
                f"awaitable must be an Awaitable, got {awaitable!r}")
        elif not isinstance(timeout, (float, int)):
            raise TypeError(
                f"timeout must be a float or integer, got {timeout!r}")
        # Start a new event loop with the awaitable in it.
        loop = asyncio.new_event_loop()
        task = loop.create_task(awaitable)
        # Use tkinter's `.after` to run the asyncio event loop.
        self.after(0, self.__advance_loop, loop, max(1, int(timeout * 1000)))
        # Run tkinter, which periodically checks
        self.mainloop()
        # After tkinter is done, wait until `asyncio` is done.
        try:
            return loop.run_until_complete(task)
        finally:
            loop.run_until_complete(loop.shutdown_asyncgens())
            loop.close()

    def destroy(self, /) -> None:
        super().destroy()
        self.is_running = False


def deg_color(deg, d_per_tick, color):
    """Helper function for updating the degree and color."""
    deg += d_per_tick
    if 360 <= deg:
        deg %= 360
        color = f"#{randrange(50):02x}{randrange(50):02x}{randrange(50):02x}"
    return deg, color


async def rotator(root, interval, d_per_tick):
    """
    An example custom method for running code asynchronously
    instead of using `tkinter.Tk.after`.

    NOTE: Code that can use `tkinter.Tk.after` is likely
          preferable, but this may not fit all use-cases and
          may sometimes require more complicated code.
    """
    canvas = tk.Canvas(root, height=600, width=600)
    canvas.pack()
    deg = 0
    arc = canvas.create_arc(
        100,
        100,
        500,
        500,
        style=tk.CHORD,
        start=0,
        extent=deg,
        fill='#%02x%02x%02x' % (int(randrange(50)), int(
            randrange(50)), int(randrange(50))),
    )
    while root.is_running:
        deg, color = deg_color(
            deg, d_per_tick, f"#{randrange(50):02x}{randrange(50):02x}{randrange(50):02x}")
        canvas.itemconfigure(arc, extent=deg, fill=color)
        await asyncio.sleep(interval)


def main():
    root = AsyncTk()
    root.run_with_mainloop(rotator(root, 1/60, 3))


if __name__ == "__main__":
    main()
