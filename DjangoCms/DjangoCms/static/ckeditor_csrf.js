function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

const csrftoken = getCookie('csrftoken');

CKEDITOR.on('instanceReady', function () {
  CKEDITOR.instances.editor1.on('fileUploadRequest', function (evt) {
      const xhr = evt.data.fileLoader.xhr;
      xhr.setRequestHeader('X-CSRFToken', csrftoken);
  });
});