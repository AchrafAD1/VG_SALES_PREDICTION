var accounts =  [
    {'team': 'data intagration', 'password': 'MDSO2024', 'path': 'data_integration.html'},
    {'team': 'data cleaning', 'password': 'MDSO2024', 'path': 'data_cleaning.html'},
    {'team': 'data science', 'password': 'MDSO2024', 'path': 'data_science.html'},
    {'team': 'testing', 'password': 'MDSO2024', 'path': 'testing.html'}
]


var form = document.querySelector('form')
var connectBtn = document.querySelector('#connectBtn')


connectBtn.addEventListener('click', () => {
    admin = false
    accounts.forEach(account => {
        console.log(form.team.value == account.team)
        console.log(form.password.value == account.password)
        if  (account.team == form.team.value && account.password == form.password.value){
            location.href = account.path
            admin = true
        }
    })
    if(!admin){
        alert('Le nom d\'équipe ou le mot de passe est n\'est pas correct!')
    }
});