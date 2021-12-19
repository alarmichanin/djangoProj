const inputChooseRailcar = document.getElementById('choose-railcar');
const arrOfRailcar = Array.from(document.getElementsByClassName('railcar'));
const arrOfRailcarNumber = Array.from(document.getElementsByClassName('railcar-number'));

arrOfRailcar.forEach((railcar, index) => {
    railcar.onclick = () => {
        inputChooseRailcar.value = arrOfRailcarNumber[index].textContent.trim();
        // railcar.classList.toggle('choosed-railcar')
    }
});