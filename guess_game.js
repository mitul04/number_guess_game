let number = null;
let guesses = 0;
let start = null;
let stop = null;

function startGame() {
    const rangeInput = document.getElementById('rangeInput').value.trim().split(' ');
    if (rangeInput.length !== 2 || isNaN(rangeInput[0]) || isNaN(rangeInput[1])) {
        alert('Please enter two valid numbers separated by a space.');
        return;
    }
    start = parseInt(rangeInput[0]);
    stop = parseInt(rangeInput[1]);
    if (start > stop) {
        alert('Start should be less than or equal to stop.');
        return;
    }
    number = Math.floor(Math.random() * (stop - start + 1)) + start;
    guesses = 0;
    document.getElementById('setup').style.display = 'none';
    document.getElementById('game').style.display = 'block';
    document.getElementById('feedback').textContent = "Let's see in how many guesses you can guess this number!";
    document.getElementById('guessInput').value = '';
}

function makeGuess() {
    const guessInput = document.getElementById('guessInput').value;
    if (guessInput === '' || isNaN(guessInput)) {
        document.getElementById('feedback').textContent = 'Please enter a valid number.';
        return;
    }
    const guess = parseInt(guessInput);
    guesses += 1;
    if (guess === number) {
        document.getElementById('feedback').textContent = `You got it right in ${guesses} guesses!`;
        document.getElementById('restartBtn').style.display = 'block';
    } else if (guess > number) {
        document.getElementById('feedback').textContent = 'You are ahead of the number.';
    } else {
        document.getElementById('feedback').textContent = 'You are behind the number.';
    }
}

function restartGame() {
    document.getElementById('setup').style.display = 'block';
    document.getElementById('game').style.display = 'none';
    document.getElementById('rangeInput').value = '';
    document.getElementById('feedback').textContent = '';
    document.getElementById('restartBtn').style.display = 'none';
}