function extractHiddenUrl(domTree) {
    const chars = [];
    
    // Use querySelectorAll to find all <i> elements that are children of the specific structure
    const elements = domTree.querySelectorAll('code[data-class][data-class*="*"] > div[data-tag][data-tag*="*"] > span[data-id][data-id*="*"] > i.char');
    
    // Loop through each found element and get its 'value' attribute
    elements.forEach(element => {
        const char = element.getAttribute('value');
        if (char) {
            chars.push(char);
        }
    });

    // Join the characters to form the final URL
    return chars.join('');
}

// Example usage with a hypothetical DOM structure
const domTree = new DOMParser().parseFromString(`
<code data-class="23*">
  <div data-tag="*93">
    <span data-id="*21*">
      <i class="char" value="h"></i>
    </span>
  </div>
  <div data-tag="*93">
    <span data-id="*21*">
      <i class="char" value="t"></i>
    </span>
  </div>
  <div data-tag="*93">
    <span data-id="*21*">
      <i class="char" value="t"></i>
    </span>
  </div>
  <div data-tag="*93">
    <span data-id="*21*">
      <i class="char" value="p"></i>
    </span>
  </div>
  <div data-tag="*93">
    <span data-id="*21*">
      <i class="char" value="s"></i>
    </span>
  </div>
  <div data-tag="*93">
    <span data-id="*21*">
      <i class="char" value="://"></i>
    </span>
  </div>
  <div data-tag="*93">
    <span data-id="*21*">
      <i class="char" value="example.com"></i>
    </span>
  </div>
</code>
`, 'text/html');

const hiddenUrl = extractHiddenUrl(domTree);
console.log(hiddenUrl); // Outputs: https://example.com