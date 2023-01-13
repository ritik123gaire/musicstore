$(
    function(){
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        let csrftoken = getCookie('csrftoken');

        $(".cart-button").click(function(){
            let productId = this.dataset.product
            let action = this.dataset.action
            let user = this.dataset.user
            console.log(productId," ",action," ",user)

            updateCartItem(productId,action)
        })

        $('.checkout-btn').click(function(){
            let cartId = this.dataset.cart
            console.log(cartId)

            updateCheckOut(cartId)
        })

        function updateCheckOut(cartId){
            var url = 'http://127.0.0.1:8000/checkout'
            fetch(url,
                {
                    method: 'POST',
                    headers:{
                        'Content-Type':'application/json',
                        'X-CSRFToken':csrftoken,
                    },
                    body: JSON.stringify({
                        'cartId':cartId,
                    })
                }
            )
            .then(response => {
                return response.json()
            })
            .then(data =>{
                console.log(data)
            })
        }

        function updateCartItem(productId,action){
            var url = 'http://127.0.0.1:8000/addToCart'
            fetch(url,
                {
                    method: 'POST',
                    headers:{
                        'Content-Type':'application/json',
                        'X-CSRFToken':csrftoken,
                    },
                    body: JSON.stringify({
                        'productId':productId,
                        'action':action
                    })
                }
            )
            .then(response => {
                return response.json()
            })
            .then(data =>{
                console.log(data)
                location.reload()
            })
        }
    }    
)