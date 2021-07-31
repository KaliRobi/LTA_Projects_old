const button = document.getElementById('button')
const toasts = document.getElementById('toasts')


const messages = [
    'becsuletsertes, 1932, no, napszamos, 2 elemi, 150 pengo, 3 nap elzaras, Derecske, ',
    'súlyos testi sértés, 1934, ferfi, foldmuves, 4 osztaly, 300 pengo, 10 nap borton, nyirbator, ',
    'jovedeki kihagas, 1938, ferfi, vasutas, vasutaskepzo, 150 pengo, 2, nap elzaras, Ebes, ',
    'maganlaksertes, 1941, no, haztartasbeli, 1 elemi, 50 pengo, 3 nap elzaras, Derecske, '


]

button.addEventListener('click', () =>  createnotification())


function createnotification() {
    var setter = console.count()
    const notif = document.createElement('div')
    notif.classList.add('toast')

    notif.innerText = getRandomMessage()
    toasts.appendChild(notif)
    
    setTimeout(()=>{
        notif.remove()
    }, 9000)
}

function getRandomMessage() {
        return messages[Math.floor(Math.random() * messages.length)]


}
/* random puls some data from the databse and sets it here, city, crime */