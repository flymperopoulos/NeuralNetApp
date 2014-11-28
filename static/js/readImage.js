$(document).ready(function(){

c = document.getElementById('simple_sketch')
ctx = c.getContext('2d');

pixels = ctx.getImageData(0,0, c.width, c.height).data;
n_pixels = c.width*c.height;
for (p=0;p<n_pixels;p++){
      var x = p%width;
        var y = Math.floor(p/width);
          Array[x][y] = [pixels[p*4],pixels[p*4+1],pixels[p*4+2]]
}

});