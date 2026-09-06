/* Pure helpers shared by practice, charts and validation. */
(function(root){
  function matchQuestion(q,{track='all',level='all',topic='all',grade='all'}={},gradeResolver=()=>[]) {
    return (track==='all'||q.track===track)&&(level==='all'||q.level===level)&&
      (topic==='all'||q.topic===topic)&&(grade==='all'||gradeResolver(q.level).includes(grade));
  }
  function formatCounts(questions,track) {
    const pool=questions.filter(q=>q.track===track);
    return {total:pool.length,mcq:pool.filter(q=>q.type==='MCQ').length,written:pool.filter(q=>q.type!=='MCQ').length};
  }
  const api={matchQuestion,formatCounts};root.PracticeCore=api;
  if(typeof module!=='undefined')module.exports=api;
})(globalThis);
