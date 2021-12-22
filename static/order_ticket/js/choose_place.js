const inputChooseRailcar = document.getElementById('choose-railcar');
const arrOfRailcar = Array.from(document.getElementsByClassName('railcar'));
const arrOfRailcarNumber = Array.from(document.getElementsByClassName('railcar-number'));

const sendButton = document.getElementById('send-btn');

sendButton.disabled = true;

arrOfRailcar.forEach((railcar, index) => {
    railcar.onclick = () => {
        inputChooseRailcar.value = arrOfRailcarNumber[index].textContent.trim();
        sendButton.disabled = inputChooseRailcar.value.length ? false : true;
    }
});

inputChooseRailcar.oninput = () => {
    sendButton.disabled = inputChooseRailcar.value.length ? false : true;
}