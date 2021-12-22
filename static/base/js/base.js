M.AutoInit();
M.updateTextFields();

const navList = document.getElementById('nav-list');

if (document.documentElement.clientWidth >= 997) {
    navList.style.marginTop = '0px';
} 

document.getElementById('nav-burger-menu').onclick = () => {
    navList.style.marginTop = navList.style.marginTop == '0px' ? '-680px' : '0px'; 
};

if (!Array.from(document.getElementById('messages').children).length) {
    document.getElementById('messages').style.display = 'none';
}
    
setTimeout(function(){
	document.getElementById('messages').style.opacity = 0;
}, 3000);