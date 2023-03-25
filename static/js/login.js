let formFields = document.querySelectorAll('#id_username, #id_password');
formFields.forEach(field => {
  field.addEventListener('focus', function() {
    this.style.transform = 'scale(1.1)';
  });
  field.addEventListener('blur', function() {
    this.style.transform = 'scale(1)';
  });
});
