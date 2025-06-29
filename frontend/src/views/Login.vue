<template>
   <div>
     <h2>Login</h2>
     <form @submit.prevent="submit">
       <input v-model="form.username" placeholder="Username" />
       <input type="password" v-model="form.password" placeholder="Password" />
       <button type="submit">Login</button>
     </form>
   </div>
</template>

<script>
import axios from 'axios'
export default {
   data() {
     return { form: { username: '', password: '' } }
   },
   methods: {
     async submit() {
       const res = await axios.post('/api/login', this.form)
       console.log(res.data)
       // TODO: obsługa tokenu, przekierowanie
     }
   }
}
</script>