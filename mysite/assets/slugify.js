const titleinput=document.querySelector('input[name=Title]');
const sluginput=document.querySelector('input[name=Slug]');

const slugify=(val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')
        .replace(/[\s\W-]+/g, '-')
};

titleinput.addEventListener('keyup',(e) => {
    sluginput.setAttribute('value', slugify(titleinput.value)); 
});