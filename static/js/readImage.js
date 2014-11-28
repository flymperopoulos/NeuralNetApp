$("#button").click( function()
   {
    var c = document.getElementById('simple_sketch')
    var ctx = c.getContext('2d');

    var pixels = ctx.getImageData(0,0, c.width, c.height).data;
    // console.log(pixels);
    var n_pixels = c.width*c.height;
    var data = new Array(c.height);
    for (row=0; row<c.height; row++) {
      data[row] = new Array(c.width);
      for (col=0; col<c.width; col++) {
        data[row][col] = pixels[row*col*4+3]/255.;
      }
    }
    var finalData = JSON.stringify(data);
    
    $.post('/', finalData, success = function(responce){
	console.log(responce);
})
});

