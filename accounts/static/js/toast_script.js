//toast calls from external js also
var ul = document.querySelector(".notifications");

function remove_ele(){
    const toast = document.querySelector('.toast');
    ul.removeChild(toast);
}

function removeToast(){
    const toast = document.querySelector('.toast');
    toast.classList.add('hide')
    setTimeout(remove_ele, 800);
}
setTimeout(removeToast, 5100);

