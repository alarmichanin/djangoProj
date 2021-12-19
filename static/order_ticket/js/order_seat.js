const inputChooseSeat = document.getElementById('choose-railcar');
const arrOfSeats = Array.from(document.getElementsByClassName('railcar'));
const arrOfSeatNumber = Array.from(document.getElementsByClassName('railcar-number'));

arrOfSeats.forEach((railcar, index) => {
    let value = inputChooseSeat.value;

    let shelf = value % 2 ? "Upper shelf" : "Lower shelf";
    railcar.innerHTML += `<p class="choose-title">${shelf}</p>`;

    railcar.onclick = () => {
        inputChooseSeat.value = arrOfSeatNumber[index].textContent.trim();
    }
});