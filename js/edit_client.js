console.log(location.search)     // lee los argumentos pasados a este formulario
var id=location.search.substr(4)  // producto_update.html?id=1
console.log(id)
const { createApp } = Vue
  createApp({
    data() {
      return {
        id:0,
        name:"", 
        lastname:"",
        dob:"",
        dni:"",
        phone:"",
        insurance:"",
        photo:"",
        url:'https://jnrosas.pythonanywhere.com/clients/'+id,
       }  
    },
    methods: {
      fetchData(url) {
        fetch(url)
          .then(response => response.json())
          .then(data => {
              console.log(data)
              this.id=data.id
              this.name = data.name
              this.lastname=data.lastname
              this.dob=data.dob
              this.dni=data.dni    
              this.phone=data.phone
              this.insurance=data.insurance
              this.photo=data.photo    
          })
          .catch(err => {
              console.error(err);
              this.error=true              
          })
      },
      modificar() {
        let client = {
          name: this.name,
          lastname: this.lastname,
          dob: this.dob,
          dni: this.dni,
          phone: this.phone,
          insurance: this.insurance,
          photo: this.photo
        }
        var options = {
          body: JSON.stringify(client),
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          redirect: 'follow'
        }
        fetch(this.url, options)
          .then(function () {
            alert("Registro modificado")
            window.location.href = "../clients.html"; // navega a index.html          
          })
          .catch(err => {
            console.error(err);
            alert("Error al Modificar")
          })      
      }
    },
    created() {
      this.fetchData(this.url)
    },
  }).mount('#app')
