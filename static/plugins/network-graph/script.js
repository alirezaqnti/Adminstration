    var data={
  "nodes":[
    {"id":"node1","group":15},
    {"id":"node2","group":2},
    {"id":"node3","group":2},
    {"id":"node4","group":3},
    {"id":"node5","group":3},
    {"id":"b1","group":3},
    {"id":"b2","group":3},

  ],
  "links":[
    {"source":"node1","target":"node3","value":1},
    {"source":"node2","target":"node1","value":2},
    {"source":"node1","target":"node4","value":1},
    {"source":"node2","target":"node5","value":1},
    {"source":"node3","target":"node5","value":1},
    {"source":"b1","target":"node1","value":1},
    {"source":"b1","target":"b2","value":1}

  ]
}
//console.log(data);

var extraNodes=[
{"id":"b3","group":3},
{"id":"node6","group":1},
{"id":"node7","group":1},
{"id":"node8","group":2},
{"id":"node9","group":2},
{"id":"node10","group":2},
{"id":"node11","group":2}
]

var extraLinks=[
{"source":"node1","target":"b3","value":2},
{"source":"b1","target":"b3","value":2},
{"source":"b1","target":"node6","value":2},
{"source":"node1","target":"node7","value":2},
{"source":"node3","target":"node8","value":2},
{"source":"node2","target":"node9","value":10},
{"source":"b1","target":"node10","value":2},
{"source":"node1","target":"node11","value":2},
]

d3.interval(function() {
  if(extraNodes.length>0){
    var _node=extraNodes.pop();
    data.nodes.push(_node);
  }
  if(extraLinks.length>0){
    var _link=extraLinks.pop();
    data.links.push(_link);
    restart();
  }
}, 1000, d3.now() + 500);

var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var color = d3.scaleOrdinal(d3.schemeCategory20c);


var simulation = d3.forceSimulation(data.nodes)
    .force("link", d3.forceLink().id(function(d) { return d.id; }).distance(60))
    .force("charge", d3.forceManyBody().strength(-20).distanceMax(100))
    .force("center", d3.forceCenter(width / 2, height / 2))
    .alphaTarget(1)

  var link = svg.append("g")
      .attr("class", "links")
      .selectAll("line")

  var node = svg.append("g")
      .attr("class", "nodes")
      .selectAll("circle")

function restart() {
  node = node.data(data.nodes, function(d) { return d.id;});
  node.exit().remove();
  node = node.enter().append("circle")
      .attr("r", function(d){
        return 10 + d.group;
      })
      .attr("fill", function(d) { return color(d.group); })
      .merge(node)
      .call(d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended));

  link = link.data(data.links, function(d) { return d.source.id + "-" + d.target.id; });
  link.exit().remove();
  link = link.enter()
            .append("line")
            .attr('stroke', color("darkgray"))
            .attr("stroke-width", function(d) { return Math.sqrt(d.value); })
            .merge(link)

  console.log(data.nodes);

  simulation
      .nodes(data.nodes)
      .on("tick", ticked);

  simulation.force("link")
      .links(data.links);

  simulation.on()

  simulation.alpha(1).restart();

  function ticked() {
    link
        .transition() // slows down the animation
        .duration(80)
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node
        .transition()
        .duration(80)
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
  }
};

// boiler plate d3 click and drag functions
function dragstarted(d) {
  if (!d3.event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(d) {
  d.fx = d3.event.x;
  d.fy = d3.event.y;
}

function dragended(d) {
  if (!d3.event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}

restart();