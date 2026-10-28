const { readFileSync } = require('node:fs');
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { JSDOM, VirtualConsole } = require('jsdom');
const html = readFileSync('docs/index.html', 'utf8');
function open(query = '') {
  const errors = [];
  const console = new VirtualConsole();
  console.on('jsdomError', error => errors.push(error.message));
  const dom = new JSDOM(html, { url: 'https://example.org/awesome-ai2-thor/' + query, runScripts: 'dangerously', virtualConsole: console });
  assert.deepEqual(errors, [], 'generated page must initialize without script errors');
  return dom;
}
function data(dom) { return JSON.parse(dom.window.document.getElementById('catalog-data').textContent); }
function count(dom) { return dom.window.document.querySelectorAll('.entry').length; }
function input(dom, id, value) {
  const element = dom.window.document.getElementById(id);
  element.value = value;
  element.dispatchEvent(new dom.window.Event('input', { bubbles: true }));
}

test('default catalog includes every native resource, with no text-only papers', () => {
  const dom = open();
  const entries = data(dom);
  assert.equal(count(dom), entries.filter(e => e.scope === 'thor-native').length);
  assert.equal(dom.window.document.querySelectorAll('.room').length, 10);
  assert.equal(dom.window.document.querySelectorAll('.entry.must-read').length, 26);
  assert.equal(dom.window.document.querySelectorAll('.adjacent-label').length, 0);
  dom.window.close();
});

test('room selection filters and deselects, preserving shareable parameters', () => {
  const dom = open();
  const button = dom.window.document.querySelector('[data-room="navigation"]');
  button.click();
  assert.equal(count(dom), data(dom).filter(e => e.scope === 'thor-native' && e.section === 'navigation').length);
  assert.equal(button.getAttribute('aria-pressed'), 'true');
  assert.equal(new URL(dom.window.location.href).searchParams.get('room'), 'navigation');
  button.click();
  assert.equal(new URL(dom.window.location.href).searchParams.has('room'), false);
  dom.window.close();
});

test('search matches titles and editorial copy without interpreting HTML', () => {
  const dom = open();
  input(dom, 'search', 'procedurally');
  const expected = data(dom).filter(e => e.scope === 'thor-native' && (e.title + ' ' + e.short + ' ' + e.highlight).toLowerCase().includes('procedurally'));
  assert.equal(count(dom), expected.length);
  assert.ok(expected.length > 0);
  input(dom, 'search', '<img src=x onerror=alert(1)>');
  assert.equal(count(dom), 0);
  assert.equal(dom.window.document.querySelectorAll('#entry-list img').length, 0);
  dom.window.document.querySelector('.empty button').click();
  assert.equal(count(dom), data(dom).filter(e => e.scope === 'thor-native').length);
  dom.window.close();
});

test('environment and year filters compose and survive a URL reload', () => {
  const dom = open('?room=navigation&env=procthor&year=2024');
  const expected = data(dom).filter(e => e.scope === 'thor-native' && e.section === 'navigation' && e.env.includes('ProcTHOR') && Number(e.year) >= 2024);
  assert.equal(count(dom), expected.length);
  input(dom, 'search', 'navigation');
  const reload = open(dom.window.location.search);
  assert.equal(count(reload), count(dom));
  assert.equal(reload.window.document.getElementById('search').value, 'navigation');
  input(dom, 'year', 2026);
  assert.ok([...dom.window.document.querySelectorAll('.year-title')].every(e => e.textContent === '2026'));
  reload.window.close();dom.window.close();
});

test('text-only appendix is opt-in and cannot alter room counts or must-reads', () => {
  const dom = open();
  const rooms = [...dom.window.document.querySelectorAll('.room-count')].map(e => e.textContent);
  const include = dom.window.document.getElementById('include-adjacent');
  include.checked = true;include.dispatchEvent(new dom.window.Event('change'));
  assert.equal(count(dom), data(dom).length);
  assert.equal(dom.window.document.querySelectorAll('.adjacent-label').length, data(dom).filter(e => e.scope === 'alfworld-adjacent').length);
  assert.equal(dom.window.document.querySelectorAll('.must-read .adjacent-label').length, 0);
  assert.deepEqual([...dom.window.document.querySelectorAll('.room-count')].map(e => e.textContent), rooms);
  assert.equal(new URL(dom.window.location.href).searchParams.get('text'), '1');
  dom.window.close();
});

test('all rooms and filters use native keyboard-focusable controls', () => {
  const dom = open();
  for (const button of dom.window.document.querySelectorAll('.room,.chip')) {
    assert.equal(button.tagName, 'BUTTON');
    assert.equal(button.type, 'button');
    button.focus();assert.equal(dom.window.document.activeElement, button);
  }
  assert.ok(html.includes('prefers-reduced-motion:reduce'));
  assert.ok(html.includes('animation:none;stroke-dashoffset:0'));
  dom.window.close();
});

test('invalid URL filters fall back safely', () => {
  const dom = open('?room=unknown&env=unknown&year=NaN');
  assert.equal(count(dom), data(dom).filter(e => e.scope === 'thor-native').length);
  dom.window.close();
});

test('family diagram parses with Mermaid and rejects invalid syntax', async () => {
  const dom = new JSDOM('');
  global.window = dom.window;global.document = dom.window.document;
  const { default: mermaid } = await import('mermaid');
  mermaid.initialize({ startOnLoad: false, securityLevel: 'strict' });
  for (const file of ['README.md', 'README.zh-CN.md']) {
    const code = readFileSync(file, 'utf8').match(/```mermaid\n([\s\S]+?)```/)[1];
    const parsed = await mermaid.parse(code);
    assert.equal(parsed.diagramType, 'flowchart-v2');
  }
  await assert.rejects(() => mermaid.parse('flowchart LR\n A[broken'));
  dom.window.close();
});
