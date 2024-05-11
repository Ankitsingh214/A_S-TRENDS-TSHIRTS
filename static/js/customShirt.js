document.addEventListener("DOMContentLoaded", function() {
  const form = document.querySelector("form");

  form.addEventListener("submit", function(event) {
    event.preventDefault(); 
    const formData = {
      username: getValue('input[name="username"]'),
      password: getValue('input[name="password"]'),
      shirtStyle: getValue('select[name="shirt-style"]'),
      fabricType: getValue('select[name="fabric-type"]'),
      color: getValue('input[name="color"]'),
      size: getValue('select[name="size"]'),
      fit: getValue('select[name="fit"]'),
      sleeveLength: getValue('select[name="sleeve-length"]'),
      neckline: getValue('select[name="neckline"]'),
      pattern: getValue('input[name="pattern"]'),
      embroidery: getValue('input[name="embroidery"]'),
      additionalFeatures: getValue('textarea[name="additional-features"]'),
      quantity: getValue('input[name="quantity"]'),
      instructions: getValue('textarea[name="instructions"]'),
      address: getValue('textarea[name="address"]'),
      email: getValue('input[name="email"]'),
      phone: getValue('input[name="phone"]'),
      payment: getValue('select[name="payment"]')
    };
    console.log(formData);

    const jsonData = JSON.stringify(formData, null, 2);

    localStorage.setItem("formData", jsonData);

    alert("Form data saved successfully!");
    console.log(jsonData);
  });

  function getValue(selector) {
    const element = form.querySelector(selector);
    return element ? element.value : '';
  }
});