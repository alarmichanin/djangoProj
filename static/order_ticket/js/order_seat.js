const inputChooseSeat = document.getElementById('choose-seat');
const arrOfSeats = Array.from(document.getElementsByClassName('seat'));
const arrOfSeatNumber = Array.from(document.getElementsByClassName('seat-number'));

arrOfSeats.forEach((seat, index) => {
    let shelf = arrOfSeats[index].textContent % 2 ? "Lower shelf" : "Upper shelf";
    seat.innerHTML += `<p class="choose-title">${shelf}</p>`;

    seat.onclick = () => {
        inputChooseSeat.value = arrOfSeatNumber[index].textContent.trim();
        console.log(inputChooseSeat.value);
    }
});