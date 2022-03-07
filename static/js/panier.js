

var updateBtns = document.getElementsByClassName('update-cart')

for(var i=0; i<updateBtns.length; i++){
     updateBtns[i].addEventListener('click',function(){
         var productId = this.dataset.product
         var action = this.dataset.action
         addCartItem(productId, action)
         console.log('USER:', user)
         if(user==='AnonymousUser'){
            addCartItem(productId, action)
         }else{
            updateUserOrder(productId, action)
         } 
     })
} 
/*
$(document).on('click', '.update-cart', function(){
    var productId = this.dataset.product
  var action = this.dataset.action
    console.log('productId:', productId, 'action:', action)
    console.log('User:', user)
    if(user === 'AnonymousUser'){
        addCartItem(productId, action)
    }else{
        updateUserOrder(productId, action)
    }

}) */

function addCartItem(productId, action){
    console.log('User is not Autenticate!')
    if(action == 'add'){
        if(cart[productId] == undefined){
            cart[productId] = {'qte_produit': 1/2}
        }else{
            cart[productId]['qte_produit'] += 1/2

        }
    }

    if(action == 'remove'){
       cart[productId]['qte_produit'] -= 1/2
       if(cart[productId]['qte_produit'] <= 0){
           console.log("Supprimer produit")
           delete cart[productId]

       }
    }
    
   
	document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
    
    /*var path = location.pathname
        console.log(path)
        if(path == '/panier/'){
            location.reload()
        }else{
            window.location.href = "panier/"
        }*/
     
}
/*
function updateUserOrder(productId, action){
    
    $.ajax({
        url : '/update_items/',
        data: {'productId': productId, 'action': action},
        dataType:'json',
        success: function(){
            location.reload()
            
        }
    })
} */

function updateUserOrder(productId, action){
    console.log('User  logged is sending data...')

    var url = '/update_items/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data:', data) 
        location.reload()
    })
} 


/*
$(document).on('click', '.update-cart', function(){
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('productId:', productId, 'action:', action)
    console.log('User:', user)

})
 

function updateUserOrder(productId, action){
		$.ajax({
			type:"POST",
			url:"{% url 'update_items' %}",
            data:{
                productId:productId,
                action:action,
                csrfMiddlewaretoken:csrftoken,
            },
			success:function(response){
				console.log(response);
			},
			error:function(response){
				//alert('error!');
			}
		})

} */