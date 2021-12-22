const sendTrainButton = document.getElementById('send-btn');
const inputIdTrain = document.getElementById('id');

sendTrainButton.disabled = true;

inputIdTrain.oninput = () => {
    sendTrainButton.disabled = inputIdTrain.value.length ? false : true;
}