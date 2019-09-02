var questionElt = document.getElementById("question");

// Pk?

$(document).ready(function(){

    $("button").click(function(){

        // $('p:last').append('<p>' + questionElt.value + '</p>');

        $.ajax({
            url : '/',
            type : 'POST',
            data : questionElt.value,

            success : function(resp){
                if (resp['histoire'] != 'vide') {
                    $('p[class="dialogue"]:last').append('<p class="dialogue">' + resp['histoire'] + '</p>');
                }
                else {
                    $('p[class="dialogue"]:last').append('<p class="dialogue">Ma mémoire doit me jouer des tours, attends...</p>');
                }
                if (resp['adresse'] != 'vide') {
                    $('p[class="dialogue"]:last').append('<p class="dialogue">Ce lieu est situé ' + resp['adresse'] + '</p>');
                    $('p[class="dialogue"]:last').append('<p class="dialogue"><iframe src=' + resp['url_carte'] + '></iframe></p>');
                }
                else {
                    $('p[class="dialogue"]:last').append('<p class="dialogue">J\'ai beau réfléchir...</p>');
                }

                $('p[class="dialogue"]:last').append('<p class="dialogue">Une autre question mon enfant ?</p>');
            }
            
            
        });

    });

});