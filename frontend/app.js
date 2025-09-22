// 获取 DOM
const modeSel = document.getElementById('mode');
const cipherSel = document.getElementById('cipher');
const runBtn = document.getElementById('run');
const outBox = document.getElementById('output');
const inputBox = document.getElementById('input');
const keyBox = document.getElementById('keyBox');

let algoList = []; // 保存 /api/list 返回的算法目录

// 1. 加载算法列表（含中文名）
async function loadAlgos() {
    const res = await fetch('/api/list');
    algoList = await res.json();
    // 填充下拉框：简写 - 中文名
    cipherSel.innerHTML = '';
    algoList.forEach(a => {
        const opt = document.createElement('option');
        opt.value = a.name_en;
        opt.textContent = `${a.name_en} - ${a.name_cn}`;
        cipherSel.appendChild(opt);
    });
    cipherSel.onchange(); // 触发一次密钥区渲染
}

// 2. 根据选中算法显示/隐藏密钥输入区
cipherSel.onchange = () => {
    const sel = algoList.find(a => a.name_en === cipherSel.value);
    if (!sel) return keyBox.innerHTML = '';
    if (!sel.need_key) return keyBox.innerHTML = '';
    // 按 key_name 生成输入框
    const names = sel.key_name.split(',');
    keyBox.innerHTML = names.map(n => `
        <label>${n.toUpperCase()}：</label>
        <input class="keyinp" data-key="${n}" placeholder="${n}">
    `).join('');
};

// 3. 运行加解密
runBtn.onclick = async () => {
    const name_en = cipherSel.value;
    const text = inputBox.value;
    const op = modeSel.value; // encrypt / decrypt
    // 收集密钥
    const key = {};
    document.querySelectorAll('.keyinp').forEach(inp => key[inp.dataset.key] = inp.value);
    const res = await fetch(`/api/${op}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name_en, text, key })
    });
    const j = await res.json();
    outBox.value = j.ok ? j.result : `❌ ${j.msg}`;
};

// 4. 初始化
loadAlgos();