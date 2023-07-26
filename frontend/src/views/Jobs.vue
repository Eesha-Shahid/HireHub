<template>
    <div>
      <Header />
      <h1>Job Listings</h1>
      <div v-if="isLoading">Loading...</div>
      <div v-else>
        <div v-if="jobs.length === 0">No jobs available.</div>
        <ul v-else>
            <li v-for="job in jobs" :key="job.id">
                <h2>{{ job.title }}</h2>
                <p>{{ job.company }}</p>
                <p>{{ job.location }}</p>
                <p>{{ job.description }}</p>
            </li>
        </ul>
      </div>
    </div>
</template>
  
<script>
    import Header from '../components/Header.vue';
    import axios from 'axios';
    
    export default {
        name: 'Jobs',

        components: {
            Header,
        },

        data() {
            return {
                jobs: [],
                isLoading: false,
            };
        },

        mounted() {
            this.fetchJobs();
        },

        methods: {

            // Sets the isLoading flag to true while waiting for the API response
            async fetchJobs() {
                try {
                    this.isLoading = true;
                    // Replace 'YOUR_BACKEND_API_ENDPOINT' with the actual API endpoint to fetch job listings
                    const response = await axios.get('http://your-django-backend-api-url/api/jobs/');
                    this.jobs = response.data;
                    this.isLoading = false;
                } catch (error) {
                    console.error('Error fetching job listings:', error);
                    this.isLoading = false;
                }
            },
        },
    };
</script>
  
<style>
    h1 {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    ul {
        list-style: none;
        padding: 0;
    }

    li {
        border: 1px solid #ddd;
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 4px;
    }

    li h2 {
        font-size: 1.8rem;
        margin-bottom: 0.5rem;
    }

    li p {
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }

    /* Loading styles */
    div[aria-busy="true"]::before {
        content: 'Loading...';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: rgba(0, 0, 0, 0.7);
        color: #fff;
        font-size: 1.5rem;
    }
</style>
  