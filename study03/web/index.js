function run_search() {
  let keyword = document.getElementById("input-name").value;
  let path = document.getElementById("path").value;
  if (!(document.getElementById('input-name').value)) {
    alert('検索キーワードが空です！');
    return;
  }

  // ここでPython側の処理を実行しに行く
  eel.search(keyword,path);
}

eel.expose(run_js_from_python);
function run_js_from_python(result) {
    document.getElementById("result").innerHTML = result;
}
