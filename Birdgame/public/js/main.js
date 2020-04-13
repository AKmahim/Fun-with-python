var _main_body = null;
var canvas = null;
var bird_div = null;
var crosshair_div = null;
var bird = null;
var bird_images = [];
var dead_birds = [];
var crosshair = null;
var score = 0;
var bullet_limit = 0;
var time_limit = 1;

function Bird(){
    this.bird_div = document.createElement('div');
    this.bird_div.id = 'bird-div-' + getRandomNum(0, 1000);
    this.bird_div.style.position = 'absolute';
    this.bird_div.style.overflow = 'hidden';
    this.bird_div.style.zIndex = '-100';
    this.posX = null;
    this.posY = null;
    canvas.appendChild(this.bird_div);
    this.bird_img = null;
    this.animate_interval = null;
    this.fly_interval = null;

    this.animate = function(direction){
        var index = direction == 'LEFT' ? 11 : 1;
        var inc = true;
        var limit = index + 8;
        var incStart = index + 1;
        this.animate_interval = setInterval(() =>{
            // var image_src = 'Bird/Untitled' + index.toString() + '.png';
//                bird_img =  document.getElementById('bird-'+ index.toString());
            bird_img =  bird_images.filter(function(elm){ return elm['id'] == ('bird-' + index.toString())})[0];
            this.bird_div.innerHTML = '';
            this.bird_div.appendChild(bird_img);
//                console.log(index);
            // bird_img.src = image_src;
            if(index > limit){
                inc = false;
            }
            if(index < incStart){
                inc = true;
            }
            if(inc){
                index++;
            }else{
                index--;
            }
        }, 20);
    }
    this.fly = function(point, angle){
//    		console.log(point);
        this.posX = point.x;
        this.posY = point.y;
        bird_speed = 15;
        if(point.x < (window.innerWidth / 2)){
//                console.log('LEFT CALLED ', point.x);
//                console.log('INNER WIDTH HALF', (window.innerWidth / 2));
            this.animate('RIGHT');
        }else{
//                console.log('RIGHT CALLED ', point.y);
//                console.log('INNER WIDTH HALF ', (window.innerWidth / 2));
            this.animate('LEFT');
        }
        this.bird_div.style.transform = 'translate(' + (point.x) + 'px,' + (point.y) + 'px)';
        this.fly_interval = setInterval(()=>{
//                rootX += 1;
//    			  rootY -= 1;
//                console.log("ROOT X", rootX);
//                console.log("ROOT Y", rootY);
            if((this.posY < (-200)) || (this.posX < (-200)) || (this.posX > (window.innerWidth + 200))){
                clearInterval(this.fly_interval);
                clearInterval(this.animate_interval);
                var old_bird = document.getElementById(this.bird_div.id);
                old_bird.remove();
                setTimeout(()=>{
                    delete this;
                    if(bullet_limit > 0 && time_limit >= 0){
                        startGameAnimation();
                    }
                }, 3000);
            }
            this.posX += bird_speed * Math.cos(angle * Math.PI / 180);
            this.posY += bird_speed * Math.sin(angle * Math.PI / 180);
            this.bird_div.style.transform = 'translate(' + (this.posX) + 'px,' + (this.posY) + 'px)';
        }, 30);
    }

    this.fadeOutEffect = function(target){
        var fadeEffect = setInterval(function () {
            if(!target.style.opacity) {
                target.style.opacity = 1;
            }
            if(target.style.opacity < 0.1) {
                clearInterval(fadeEffect);
                target.remove();
            } else {
                target.style.opacity -= 0.1;
            }
        }, 50);
    }

    this.stopFly = function(){
        clearInterval(this.fly_interval);
        clearInterval(this.animate_interval);
//            console.log(this.bird_div.id);
        var old_bird = document.getElementById(this.bird_div.id);
//            console.log(old_bird);
        old_bird.style.opacity = 1;
        this.fadeOutEffect(old_bird);
        setTimeout(()=>{
            delete this;
            if(bullet_limit > 0 && time_limit >= 0){
                startGameAnimation();
            }
        }, 3000);
    }
}

function setGameCanvas(){
    _main_body = document.body;
    canvas = document.getElementById('canvas');
    _main_body.style.height = window.innerHeight - 16 + 'px';
    canvas.style.width = (window.innerWidth - 16) + 'px';
    // canvas.style.height = window.innerHeight - 16 + 'px';
    // canvas.style.height = 'inherit';

    // CREATE CROSSHAIR DIV
    crosshair_div = document.createElement('div');
    canvas.appendChild(crosshair_div);
    crosshair_div.id = 'crosshair-div';
    crosshair_div.style.position = 'absolute';
    crosshair_div.style.overflow = 'hidden';
    initCrossHair();
    for(var i = 1; i < 21; i++){
        var bird_image = new Image();
        bird_image.id = 'bird-' + i.toString();
        bird_image.src = 'images/bird/Untitled' + i.toString() + '.png';
        bird_image.width = '128';
        bird_image.height = '128';
        bird_image.style.bottom = '0';
        bird_image.style.left = '0';
        bird_images.push(bird_image);
//            _main_body.appendChild(bird_image);
    }
}

function initCrossHair(){
    crosshair = document.createElement('img');
    crosshair.src = 'images/crosshair.png';
    crosshair.width = '32';
    crosshair.height = '32';
    crosshair_div.appendChild(crosshair);
}

function startGameAnimation(){
    bird = new Bird;
//        bird.animate();
    var x = getRandomNum(100, (window.innerWidth - 100));
//        var x = window.innerWidth/2;
    var y = (window.innerHeight - 100);
//        var y = window.innerHeight/2;
    var point = {'x' : x, 'y' : y};
    var angle = processAngle(x);
//        console.log("POINT ", point);
//        console.log("Angle ", angle);
    bird.fly(point, angle);
}

function startTimer(){
    var min = 4;
    var sec = 30;
    var time_lim_interval = setInterval(function(){
        document.getElementById('time-limit').innerHTML = min + ':' + (sec < 10 ? '0' + sec : sec);
        sec -= 1;
        if(sec == 0){
            min -= 4;
            sec = 59;
            time_limit -= 1;
        }
        if(min < 0){
            endGame();
            clearInterval(time_lim_interval);
        }
    }, 1000);
}

function getRandomNum(min,max){
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function processAngle(x_axis_point){
    if(x_axis_point < (window.innerWidth / 2)){
        return getRandomNum(271, 340);
    }else{
        return getRandomNum(200, 270);
    }
}

window.onload = function(){
    setGameCanvas();
//        startGameAnimation();
}

document.onmousemove = function(event){
    if(bullet_limit > 0 && time_limit >= 0){
        var mouseX = event.clientX;
        var mouseY = event.clientY;
        // console.log(mouseX + ' : ' + mouseY);
        crosshair_div.style.transform = 'translate(' + (mouseX - 32) + 'px,' + (mouseY - 32) + 'px)';
        canvas.style.cursor = 'none';
    }
}

function birdIsShot(m, b){
    if((m.x >= (b.x+32) && m.x <= (b.x + 128)) && (m.y >= (b.y+32) && m.y <= (b.y + 128))){
        return true;
    }
    return false;
}

function gunBang(){
    var audio = document.createElement("audio");
    audio.src = "audio/gun_fire.mp3";
    audio.play();
    audio.addEventListener("ended", function(e){
//            console.log(e);
//            console.log(this);
//            document.removeChild(this);
    }, false);
}

function decreaseBullet(){
    bullet_limit -= 1;
    document.getElementById('bullet-limit').innerHTML = bullet_limit;
}

function setGameScore(){
    document.getElementById('game-score').innerHTML = score;
}

function startGame(){
    bullet_limit = 100;
    score = 0;
    document.getElementById('start-game-btn').style.display = 'none';
    document.getElementById('game-end-score-board').style.display = 'none';
    setGameScore();
    startTimer();
    startGameAnimation();
}

function endGame(){
    document.getElementById('game-end-score-board').style.display = 'block';
    document.getElementById('game-end-score').innerHTML = score;
    canvas.style.cursor = 'default';
    setTimeout(()=>{
        document.getElementById('start-game-btn').style.display = 'block';
    }, 5000);
}

document.onclick = function(event){
    console.log(event.which);
    var mouseX = event.clientX;
    var mouseY = event.clientY;
    if(event.which == 1 && bullet_limit > 0 && time_limit >= 0){
        var mouse_point = {"x": mouseX, "y": mouseY};
        var bird_point = {"x": bird.posX, "y": bird.posY};
        decreaseBullet();
        gunBang();
        if((dead_birds.indexOf(bird.bird_div.id) < 0) && birdIsShot(mouse_point, bird_point)){
//            for(elm in dead_birds){
//                console.log(dead_birds[elm]);
//            }
//            console.log(bird.bird_div.id);
            dead_birds.push(bird.bird_div.id);
            var death_sound = document.getElementById("death-sound");
            death_sound.play();
            bird.stopFly();
            score += 1;
            setGameScore();
        }
        if(bullet_limit == 0 || time_limit < 0){
            endGame();
        }
    }
}

//this.x += this.speed * Math.cos(angle * Math.PI / 180);
//this.y += this.speed * Math.sin(angle * Math.PI / 180);