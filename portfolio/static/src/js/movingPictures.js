/**
 * Created by toby on 11/3/16.
 */
(function (){
    "use strict";
    //Instance variables
    var imageArray = [];
    var x = 0;
    var y = 0;

// get canvas element.
    /*var elem = document.getElementById('myCanvas');
    elem.style.height = '100%';
    elem.style.width = '100%';
    var context = ctx;*/

//The initialization method that... initializes
    init();

//Object for the images on the canvas, can be moved and resized
//resourced and instantiates Image(), Need to make type of image though
    function MakePictureObj(){
        new Image(this);
        this.image= new Image();
        this.src= "{% static 'src/img/picture2.jpg'%}";
        this.x = 0;
        this.y = 0;
        this.sizeX = 200;
        this.sizeY = 200;
        this.originalX = 9999;
        this.originalY = 9999;
        this.fadeIn = false;
        this.fadeOut = false;

        this.animationStrategy = function(){
            animate1(this);
        };

        this.deltaX = function(){
            return (this.x - this.originalX);
        };

        this.deltaY = function(){
            return (this.y - this.originalY)
        }
    }

//changes the X and Y values of the Picture object with a little bounds detection
    function animateRight(obj){

        if(obj.x > 840){
            obj.x = obj.originalX;
        }else {
            obj.x += 1;
        }
    }
    function animateLeft(obj){

        if(obj.x < 0){
            obj.x = obj.originalX;
        }else {
            obj.x -= 1;
        }
    }

    var p = {x:25, y:25};
    var velo=1, corner=60, rad=200;
    var fadePercentage = 0;

    var moveX=Math.cos(Math.PI/180*corner) * velo;
    var moveY=Math.sin(Math.PI/180*corner) * velo;

    function animate1(obj){
        //context.clearRect(0,0, elem.width, elem.height);

        if(obj.x>elem.width-rad || obj.x<rad) moveX=-moveX;
        if(obj.y>elem.height-rad || obj.y<rad) moveY=-moveY;

        obj.x +=moveX;
        obj.y +=moveY;

        context.beginPath();
        context.arc(obj.x, obj.y, rad, 0 , Math.PI*2,false);
        context.closePath();

    }

//Creates objects and adds to imageArray
//Then modifies the objects based on where on the canvas they will be
//Currently set for a 5 x 4 grid on x=1000 size canvas
    function init(){
        for(var j = 0; j < 16; j++){

            imageArray[j] = new MakePictureObj();

            //base case, start of loop BUT still step x by 200
            if(j == 0 && x == 0){
                imageArray[j].originalX = 0;
                imageArray[j].originalY = 0;

            }else if (j != 0 && x < 800){
                //NOT the beginning of the loop && not the end
                x += 200;
                imageArray[j].originalX = x;
                imageArray[j].originalY = y;
                imageArray[j].x = x;
                imageArray[j].y = y;

            }else {
                //The END reset
                y += 200;
                x = 0;
                imageArray[j].originalX = x;
                imageArray[j].originalY = y;
                imageArray[j].x = 0;
                imageArray[j].y = y;
            }
            if ((j%2) == 0){
                imageArray[j].src = "{% static 'src/img/picture1.jpg'%}";
                imageArray[j].animationStrategy = function(){
                    animateRight(this);
                }
            }
            if ((j%8) == 0){
                imageArray[j].fadeIn = true;
                imageArray[j].src = "{% static 'src/img/picture3.jpg'%}";
                imageArray[j].animationStrategy = function(){
                    animateLeft(this);

                }
            }
        }
    }

//Moves all the elements in the imageArray, but only every fourth
    function moveStuff(){

        requestAnimationFrame(moveStuff);

        context.clearRect(0,0, elem.width, elem.height);

        for(var i = 0; i < imageArray.length; i++){
            var obj = imageArray[i];

            obj.animationStrategy();

            //If it's the object to be faded
            if (obj.fadeIn == true || obj.fadeOut == true){

                //call fade on the object that's flagged to be faded
                fade(obj);
            }
            //It's NOT the object to be faded
            else{
                context.save();
                roundedImage(obj.x, obj.y, 200, 200, 20);
                context.clip();
                context.drawImage(obj.image, obj.x, obj.y, obj.sizeX, obj.sizeY);
                context.restore();

            }
        }
    }

    function fade(obj){

        context.save();
        context.globalAlpha = fadePercentage/100;
        roundedImage(obj.x, obj.y, 200, 200, 20);
        context.clip();
        context.drawImage(obj.image, obj.x, obj.y, obj.sizeX, obj.sizeY);
        context.restore();


        if (fadePercentage >= 100 && obj.fadeIn == true){
            obj.fadeIn = false;
            obj.fadeOut = true;

        }else if (fadePercentage < 100 && obj.fadeIn == true){
            fadePercentage+= .5;

        }else if(fadePercentage >= 0 && obj.fadeOut == true){
            fadePercentage -= .5;

        }else if(fadePercentage < 0 && obj.fadeOut == true){
            obj.fadeOut = false;
            obj.fadeIn = true;

            tempSRC = obj.image;
            tempSRC.src = imageArray[Math.floor(Math.random()*(16))].src;
        }
    }
//Draws the image after being loaded
    window.onload = function() {

        for(var i = 0; i < imageArray.length; i++){

            //Don't know why I need these two unless the Image function isn't
            //being called when the object is initially created but does so below
            var tempImg = imageArray[i].image;
            tempImg.src = imageArray[i].src;

            context.drawImage(imageArray[i].image, imageArray[i].x, imageArray[i].y, imageArray[i].sizeX, imageArray[i].sizeY);
        }
        moveStuff();
    };

    function roundedImage(x, y, width, height, radius) {

        context.beginPath();
        context.moveTo(x + radius, y);
        context.lineTo(x + width - radius, y);
        context.quadraticCurveTo(x + width, y, x + width, y + radius);
        context.lineTo(x + width, y + height - radius);
        context.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
        context.lineTo(x + radius, y + height);
        context.quadraticCurveTo(x, y + height, x, y + height - radius);
        context.lineTo(x, y + radius);
        context.quadraticCurveTo(x, y, x + radius, y);
        context.closePath();

    }

    var count = 0;

    addEventListener('message', function (event) {
        // doesn't matter what the message is, just toggle the worker
        if (running === false) {
            postMessage("Starting...");
            count = 0;
            running = true;
            compute(1);
        } else {
            postMessage("Stopping...");
            running = false;
        }
    })
}());

