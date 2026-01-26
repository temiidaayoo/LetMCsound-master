<template>
    <div>
        <section 
        class="banner" 
        style="background-image: url('/assets/fondo.png'); 
        background-size: cover;
        background-position: center; 
        background-repeat: no-repeat;">
        <img src="/assets/letmc.png" alt="Overlay">
        </section>

        <section class="section">
        <h2>Recent</h2>
        <div class="card-grid">
            <div class="card" style="background-image: url('/assets/musicians.png'); background-size: cover;" @click="$router.push('/sound')">
            <h3>Sounds</h3>
            <p>Browse beats, melodies and samples here.</p>
            </div>
            <div class="card" style="background-image: url('/assets/musicians.png'); background-size: cover;" @click="$router.push('/musicians')">
            <h3>Musicians</h3>
            <p>Listen to musicians here.</p>
            </div>
            <div class="card" style="background-image: url('/assets/lyrics.png'); background-size: cover;" @click="$router.push('/lyrics')">
            <h3>Lyrics</h3>
            <p>Browse through lyrics here.</p>
            </div>
        </div>
        </section>

        <section class="section">
        <h2>Popular Right Now</h2>
        <div class="card-grid">
            <div class="card" style="background-image: url('/assets/musicians.png'); background-size: cover;">
            <h3>Film Makers</h3>
            <p>Check some videos here.</p>
            </div>
            </div>
        </section>
    </div>
</template>