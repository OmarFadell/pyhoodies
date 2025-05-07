<template>
    <footer class="footer">
        <div class="footer-links">
            <a href="#" class="footer-link">All Products</a>
            <a href="#" class="footer-link">About</a>
            <a href="#" class="footer-link">Services</a>
            <a href="#" class="footer-link">Contact</a>
        </div>
        <div class="footer-logo">
            <img src="../assets/wlogo.png" alt="Logo" />
        </div>
    </footer>
</template>

<script>
export default {
    name: "Footer",
};
</script>

<style scoped>
.footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: black;
    color: white;
    padding: 20px;
    height: 30vh;
    width: 100%;
}

.footer-links {
    display: flex;
    flex-direction: column;
    /* border: 1px solid white; */
    height: 100%;
    width: 100%;
    margin-left: 2rem;
}

.footer-link {
    color: white;
    text-decoration: none;
    margin-bottom: 10px;
    font-family: 'Red Hat Display', sans-serif;
    font-size: 2rem;
    text-align: left;
}

.footer-link:hover {
    text-decoration: underline;
}

.footer-logo img {
    opacity: 0.5;
    max-width: 400px;
}

@media (max-width: 768px) {
    .footer {
        /* flex-direction: column; */
        align-items: center;
        height: auto;
    }

    .footer-links {
        margin-left: 0;
        text-align: center;
        
        
    }

    .footer-logo img {
        max-width: 200px;
        margin-right: 30px;
    }
    
}
</style>