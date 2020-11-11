'use strict';

var btnSMix = document.getElementById('select-mixto');
btnSMix.addEventListener('click',function(){
    let currentUrl = window.location.href;
    window.location.replace(currentUrl + 'mixto');
});

var btnSMult = document.getElementById('select-multiplicativo');
btnSMult.addEventListener('click',function(){
    let currentUrl = window.location.href;
    window.location.replace(currentUrl + 'multiplicativo');
});