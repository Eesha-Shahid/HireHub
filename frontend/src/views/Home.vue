
<template>
    <div>
        <Header />
        <h1>Welcome to HireHub!</h1>
        <p>Find your dream job here.</p>
    </div>
</template>
  
<script>
    import Header from '../components/Header.vue';
    
    export default {
        name: 'Home',
        components: {
            Header,
        },
    };
</script>
  
<style>
    h1 {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    p {
        font-size: 1.2rem;
        line-height: 1.6;
        max-width: 600px;
        margin-bottom: 2rem;
    }
</style>
  