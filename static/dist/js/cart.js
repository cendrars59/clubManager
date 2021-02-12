// Script in order to manage the training cart .

var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var practiceId = this.dataset.product
        var action = this.dataset.action 
        console.log('practiceId:', practiceId, 'action:', action)
    })
}
