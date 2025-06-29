<template>
   <div>
     <h2>Your Profile</h2>
     <!-- TODO: pobranie danych użytkownika -->
     <p>Username: {{ user.username }}</p>
     <p>Email: {{ user.email }}</p>
     <p>Bio: {{ user.bio }}</p>
   </div>
</template>

<script>
export default {
   data() {
     return { user: {} }
   },
   async mounted() {
     const res = await this.$axios.get('/api/profile')
     this.user = res.data
   }
}
</script>