if (localStorage.getItem("access_token") === null) {
    window.location.href= "/login";
}

function logout() {
    localStorage.removeItem("access_token");
    sessionStorage.removeItem("username");
    sessionStorage.removeItem("email");
    sessionStorage.removeItem("role");
    window.location.href= "/";
}

if (localStorage.getItem("access_token") === null) {
    window.location.href= "/login";
<<<<<<< HEAD
}

function Dashboard(){
    window.location.href="/Dashboard"
=======
>>>>>>> d29e972 (eight commit)
}