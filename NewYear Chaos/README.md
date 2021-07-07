<div class="hackdown-content">
    <p>It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their <em>initial</em> position in the queue from <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.162ex" height="2.176ex" style="vertical-align: -0.338ex;" viewBox="0 -791.3 500.5 936.9" role="img" focusable="false"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><path stroke-width="1" d="M213 578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z"></path></g></svg></span> to <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-2-Frame"></span>. Any person can bribe the person <em>directly in front</em> of them to swap positions, but they still wear their original sticker. One person can bribe <em>at most two others</em>.  </p>

<p>Determine the minimum number of bribes that took place to get to a given queue order.  Print the number of bribes, or, if anyone has bribed more than two people, print <code>Too chaotic</code>.</p>

<p><strong>Example</strong>  </p>

<p><span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-3-Frame"></span>   </p>

<p>If person <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-4-Frame"></span> bribes person <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-5-Frame"></span>, the queue will look like this: <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-6-Frame"></span>.  Only <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-7-Frame"></span> bribe is required. Print <code>1</code>.</p>

<p><span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-8-Frame"></span>  </p>

<p>Person <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-9-Frame"></span> had to bribe <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-10-Frame"></span> people to get to the current position.  Print <code>Too chaotic</code>.  </p>

<p><strong>Function Description</strong></p>

<p>Complete the function <em>minimumBribes</em> in the editor below.  </p>

<p>minimumBribes has the following parameter(s):</p>

<ul>
<li><em>int q[n]</em>: the positions of the people after all bribes    </li>
</ul>

<p><strong>Returns</strong>  </p>

<ul>
<li>No value is returned.  Print the minimum number of bribes necessary or <code>Too chaotic</code> if someone has bribed more than <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-11-Frame"></span> people.  </li>
</ul></div>

<p><strong>Input Format</strong></p>

<p>The first line contains an integer <span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" id="MathJax-Element-1-Frame"></span>, the number of test cases.   </p>

<p>Each of the next </span> pairs of lines are as follows: <br>
- The first line contains an integer, the number of people in the queue <br>
- The second line has space-separated integers describing the final state of the queue.  
</p>

<p><b>Sample Input
</b></p>
<div class="tg-wrap"><table class="tg">
<thead>
  <tr>
    <th class="tg-0lax">STDIN</th>
    <th class="tg-0lax">FUNCTION</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">2</td>
    <td class="tg-0lax">t = 2</td>
  </tr>
  <tr>
    <td class="tg-0lax">5</td>
    <td class="tg-0lax">n = 5</td>
  </tr>
  <tr>
    <td class="tg-0lax">2 1 5 3 4 </td>
    <td class="tg-0lax">q = [2, 1, 4, 3, 4] </td>
  </tr>
  <tr>
    <td class="tg-0lax">5</td>
    <td class="tg-0lax">n = 5</td>
  </tr>
  <tr>
    <td class="tg-0lax">2 1 5 3 4 </td>
    <td class="tg-0lax">q = [2, 5, 1, 3, 4] </td>
  </tr>
</tbody>
</table></div>

<p><b>Sample Output
</b></p>

<div class="tg-wrap"><table class="tg">
<thead>
  <tr>
    <th class="tg-0lax">3</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">Too chaotic&nbsp;&nbsp;&nbsp;&nbsp;</td>
  </tr>
</tbody>
</table></div>
