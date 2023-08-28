
function startTalk(_type){
    if (_type == 0){
        window.open("https://wa.me/+9720546761266?text=היי!, אשמח להשכיר ציוד לתאריך","_blank")
    }
    else if (_type == 1){
        location.href = "tel:0529171171";
    }
    else{
        /* somthing broken */
        location.href = "tel:0546761266"
    }

}