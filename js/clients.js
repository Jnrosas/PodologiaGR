const { createApp } = Vue
  createApp({
    data() {
      return {
        clients:[],
        //url:'http://localhost:5000/clients', 
        // si el backend esta corriendo local usar localhost 5000(si no lo subieron a pythonanywhere)
        url:'https://jnrosas.pythonanywhere.com/clients',
        error:false,
        cargando:true,
        /*atributos para guardar los valores del formulario */
        id:0,
        name:"", 
        lastname:"",
        dob:"",
        dni:"",
        phone:"",
        insurance:"",
        photo:""
      }  
    },
    methods: {
      fetchData(url) {
        fetch(url)
          .then(response => response.json())
          .then(data => {
            this.clients = data;
            this.cargando=false
          })
          .catch(err => {
            console.error(err);
            this.error=true              
          })
      },
      eliminar(id) {
        const url = this.url+'/' + id;
        var options = {
            method: 'DELETE',
        }
        fetch(url, options)
          .then(res => res.json()) // or res.text()
          .then(res => {
            alert('Registro Eliminado')
            location.reload(); // recarga el json luego de eliminado el registro
          })
      },
      grabar(){
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
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          redirect: 'follow'
        }
        fetch(this.url, options)
          .then(function () {
            alert("Registro grabado")
            window.location.href = "../clients.html";  // recarga clients.html
          })
          .catch(err => {
            console.error(err);
            alert("Error al Grabar")  // puedo mostrar el error tambien
          })      
      }
    },
    created() {
        this.fetchData(this.url)
    },
  }).mount('#app')
