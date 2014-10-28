function( window ){

    var body = document.body,
        mask = document.createElement("div"),
        toggleSlideLeft = document.querySelector( ".toggle-slide-left" ),
        toggleSlideRight = document.querySelector( ".toggle-slide-right" ),
        toggleSlideTop = document.querySelector( ".toggle-slide-top" ),
        toggleSlideBottom = document.querySelector( ".toggle-slide-bottom" ),
        togglePushLeft = document.querySelector( ".toggle-push-left" ),
        togglePushRight = document.querySelector( ".toggle-push-right" ),
        togglePushTop = document.querySelector( ".toggle-push-top" ),
        togglePushBottom = document.querySelector( ".toggle-push-bottom" ),
        slideMenuLeft = document.querySelector( ".slide-menu-left" ),
        slideMenuRight = document.querySelector( ".slide-menu-right" ),
        slideMenuTop = document.querySelector( ".slide-menu-top" ),
        slideMenuBottom = document.querySelector( ".slide-menu-bottom" ),
        pushMenuLeft = document.querySelector( ".push-menu-left" ),
        pushMenuRight = document.querySelector( ".push-menu-right" ),
        pushMenuTop = document.querySelector( ".push-menu-top" ),
        pushMenuBottom = document.querySelector( ".push-menu-bottom" ),
        activeNav
    ;
    mask.className = "mask";

toggleSlideTop.addEventListener( "click", function(){
        classie.add( body, "smt-open" );
        document.body.appendChild(mask);
        activeNav = "smt-open";