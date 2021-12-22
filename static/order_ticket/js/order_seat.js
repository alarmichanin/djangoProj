const inputChooseSeat = document.getElementById('choose-seat');
const arrOfSeats = Array.from(document.getElementsByClassName('seat'));
const arrOfSeatNumber = Array.from(document.getElementsByClassName('seat-number'));

const sendSeatButton = document.getElementById('send-seat-btn');
sendSeatButton.disabled = true;

arrOfSeats.forEach((seat, index) => {
    let shelf = arrOfSeats[index].textContent % 2 ? "Lower shelf" : "Upper shelf";
    seat.innerHTML += `<p class="choose-title">${shelf}</p>`;

    seat.onclick = () => {
        inputChooseSeat.value = arrOfSeatNumber[index].textContent.trim();
        sendSeatButton.disabled = false;
    }
});

inputChooseSeat.oninput = () => {
    sendSeatButton.disabled = inputChooseSeat.value.length ? false : true;
}