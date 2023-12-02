function updatePreview() {
    const editor = document.getElementById('editor');
    const preview = document.getElementById('preview');
    const markdown = editor.value;
    
    // Enable the breaks option to interpret carriage returns
    const html = marked(markdown, { breaks: true });
    
    preview.innerHTML = html;
  }

  // Call updatePreview when the page loads
  window.onload = updatePreview;