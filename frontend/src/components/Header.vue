<template>
    <header>

        <nav>
            <router-link to="/">Home</router-link>
            <router-link to="/jobs">Jobs</router-link>
        </nav>

        <div class="user-section">
            <div v-if="isLoggedIn">
                <span>Welcome, {{ username }}</span>
                <button @click="logout">Logout</button>
            </div>
            <div v-else>
                <router-link to="/login">Login</router-link>
                <router-link to="/register">Register</router-link>
            </div>
        </div>
        
    </header>
  </template>
  
  <script>
  export default {
    name: 'Header',
    data() {
      return {
        isLoggedIn: false,
        username: '',
      };
    },
    mounted() {
      // Check if the user is logged in and update the isLoggedIn and username variables accordingly
      // For example, you can use cookies or local storage to store the user's login status and information
      // For the sake of this example, we'll assume the user is not logged in initially
      this.isLoggedIn = false;
      this.username = '';
    },
    methods: {
      logout() {
        // Implement the logout functionality here
        // For example, clear the user's login status and information from cookies or local storage
        // For the sake of this example, we'll simply set isLoggedIn to false and clear the username
        this.isLoggedIn = false;
        this.username = '';
      },
    },
  };
  </script>
  
<style>
    header {
        background-color: #333;
        color: #fff;
        padding: 1rem;
    }

    nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    nav a {
        color: #fff;
        text-decoration: none;
        margin-right: 1rem;
    }

    .user-section {
        margin-top: 1rem;
        display: flex;
        justify-content: flex-end;
    }

    .user-section span {
        margin-right: 1rem;
    }

    .user-section button {
        background-color: #fff;
        color: #333;
        border: none;
        cursor: pointer;
        padding: 0.5rem 1rem;
    }
</style>
  