$(function() {
    $.FroalaEditor.DefineIcon('code', {NAME: 'code'});
    $.FroalaEditor.RegisterCommand('code', {
      title: 'Code',
      type: 'dropdown',
      focus: false,
      undo: false,
      refreshAfterCallback: true,
      options: {
        'python': 'Python',
        'html': 'HTML',
        'css': 'CSS',
      },
      callback: function (cmd, val) {
            this.html.insert('<pre><code class="' + val + '">' + this.html.getSelected () + '</code><pre>');
      },
    });

    $('#id_body').froalaEditor({
        heightMin: 350,

        toolbarButtons: [
            'fullscreen', 'bold', 'italic', 'underline', 'strikeThrough', 'subscript', 'superscript',  'code', '|',
            'fontFamily', 'fontSize', 'color', 'inlineClass', 'inlineStyle', 'paragraphStyle', 'lineHeight',
            '|', 'paragraphFormat', 'align', 'formatOL', 'formatUL', 'outdent', 'indent', 'quote', '-',
            'insertLink', 'insertImage', 'insertVideo', 'embedly', 'insertFile', 'insertTable', '|',
            'emoticons', 'fontAwesome', 'specialCharacters', 'insertHR', 'selectAll', 'clearFormatting',
            '|', 'print', 'getPDF', 'spellChecker', 'help', 'html', '|', 'undo', 'redo']
    })
});