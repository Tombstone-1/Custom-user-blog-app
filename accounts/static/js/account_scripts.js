
// show/hide password
function toggle_pass (){
    var ele1 = document.getElementById('id_pass1');
    var ele2 = document.getElementById('id_pass2')

    if (ele2 != null){
        if (ele1.type == "password" && ele2.type == "password"){
            ele1.type = "text"
            ele2.type = "text"
        } else {
            ele1.type = "password"
            ele2.type = "password"
        }
    } else {
        if (ele1.type == "password"){
            ele1.type = "text"
        }else{
            ele1.type = "password"
        }
    }
}

// form validations and error passing to modal:
function validateForm() {
    var returnval = true
    var password = document.forms['signup_form']["password1"].value
    var cpassword = document.forms['signup_form']["password2"].value

    if (password.length < 8){
        returnval = false
        let message = 'Password Should Contain Character between 8 - 15.';
        let status = 'warning';
        let icon = 'fa-circle-info';
        createToast(message, status, icon);
        
    } 
    else if (password != cpassword) { 
        returnval = false
        let message = 'Password and Confirm Password did not Match.';
        let status = 'info';
        let icon = 'fa-triangle-exclamation';
        createToast(message, status, icon);
        
    }
    else {
        returnval = true
    }

    return returnval
}

function createToast(message, status, icon) {
    const ul = document.querySelector(".notifications");
    var li = document.createElement("li");
    li.className = `toast ${status}`;
    li.innerHTML = `<div class = "column">
                        <i class="fa-solid ${icon}"></i>
                        <span>${message}</span>
                    </div>
                    <i class="fa-solid fa-xmark" onclick="removeToast()"></i>`;
    ul.appendChild(li);
    setTimeout(removeToast, 5100);
}

