const replyBtns = document.querySelectorAll(".reply-btn");
replyBtns.forEach(btn => {
    btn.addEventListener('click', (e)=> {
        e.preventDefault();
        if(e.target.nextElementSibling.style.display==="block"){
            e.target.nextElementSibling.style.display="none"
        }else{
            e.target.nextElementSibling.style.display="block"
        }
    })
})