from browser import document, window


def click(ev):
    firstname = document['firstname'].value
    lastname = document['lastname'].value
    if not firstname or not lastname:
        return
    window.open(
        f"/chat?firstname={firstname}&lastname={lastname}")


document["login"].bind("click", click)
