M.AutoInit();

M.updateTextFields();

document.getElementById('nav-burger-menu').onclick = () => {
    const navList = document.getElementById('nav-list');
    navList.style.marginTop = navList.style.marginTop == '0px' ? '-310px' : '0px'; 
};