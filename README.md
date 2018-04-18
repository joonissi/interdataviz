# Interactive Data Visualization


## TODOS

- Source code
  - API/DATA?
  - D3.js
- Report (3-6 pages)
  - the chosen data; the questions you want to answer through visualizing the data;

  - your design rationale following Munzner's model of visualization design and validation (clearly explaining the data abstraction, the task abstraction, the visual idiom and visual encoding) and other principles discussed in the course, e.g., Tufte's principles and Gestalt laws;
  - the insights, like observations and discovery, you get after visualizing your data including answers to your initial questions;
  - the limitations of the visualization;
  - each member's contribution to the project;
  - references.
  
- Presentation (pdf)


## d3.js demos


<meta charset="utf-8">
<style>

.area {
  fill: steelblue;
  clip-path: url(#clip);
}

</style>
<svg width="660" height="500"></svg>
<script src="https://d3js.org/d3.v4.min.js"></script>
<script>

var svg = d3.select("svg"),
    margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom;

var parseDate = d3.timeParse("%b %Y");

var x = d3.scaleTime().range([0, width]),
    y = d3.scaleLinear().range([height, 0]);

var xAxis = d3.axisBottom(x),
    yAxis = d3.axisLeft(y);

var zoom = d3.zoom()
    .scaleExtent([1, 32])
    .translateExtent([[0, 0], [width, height]])
    .extent([[0, 0], [width, height]])
    .on("zoom", zoomed);

var area = d3.area()
    .curve(d3.curveMonotoneX)
    .x(function(d) { return x(d.date); })
    .y0(height)
    .y1(function(d) { return y(d.price); });

svg.append("defs").append("clipPath")
    .attr("id", "clip")
  .append("rect")
    .attr("width", width)
    .attr("height", height);

var g = svg.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.csv("sp500.csv", type, function(error, data) {
  if (error) throw error;

  x.domain(d3.extent(data, function(d) { return d.date; }));
  y.domain([0, d3.max(data, function(d) { return d.price; })]);

  g.append("path")
      .datum(data)
      .attr("class", "area")
      .attr("d", area);

  g.append("g")
      .attr("class", "axis axis--x")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  g.append("g")
      .attr("class", "axis axis--y")
      .call(yAxis);

  var d0 = new Date(2003, 0, 1),
      d1 = new Date(2004, 0, 1);

  // Gratuitous intro zoom!
  svg.call(zoom).transition()
      .duration(1500)
      .call(zoom.transform, d3.zoomIdentity
          .scale(width / (x(d1) - x(d0)))
          .translate(-x(d0), 0));
});

function zoomed() {
  var t = d3.event.transform, xt = t.rescaleX(x);
  g.select(".area").attr("d", area.x(function(d) { return xt(d.date); }));
  g.select(".axis--x").call(xAxis.scale(xt));
}

function type(d) {
  d.date = parseDate(d.date);
  d.price = +d.price;
  return d;
}

</script>





