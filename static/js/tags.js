function change_status(id) {
    var searchParams = new URLSearchParams(window.location.search);
    if (searchParams.has(id)) {
        searchParams.delete(id)
    } else {
        searchParams.append(id, id)
    }
    window.location.search = searchParams.toString()
}