document.addEventListener("DOMContentLoaded", function (event) {
   let  sc = document.createElement('script')
   sc.setAttribute('src' , "https://cdn.tiny.cloud/1/k4t1cofo1ajccl0csaav8l266oqd3yx6snlp06x2bnhdczc1/tinymce/5/tinymce.min.js");
   document.head.appendChild(sc);
   sc.onload= ()=>{
      tinymce.init({
        selector: '#id_content'
});
   }
});
