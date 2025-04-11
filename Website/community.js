// Community Page JavaScript
document.addEventListener('DOMContentLoaded', function() {
    const forumPostsContainer = document.getElementById('forum-posts');
    const eventsListContainer = document.getElementById('events-list');
    
    // Sample forum posts data
    const forumPostsData = [
        {
            id: 1,
            title: "Tips for organic pest control in vegetable farming",
            author: "Rajesh Singh",
            replies: 24,
            status: "Hot Topic"
        },
        {
            id: 2,
            title: "Water-saving irrigation techniques for rice cultivation",
            author: "Meena Kumari",
            replies: 17,
            status: "Expert Thread"
        },
        {
            id: 3,
            title: "Best practices for greenhouse tomato production",
            author: "Amit Patel",
            replies: 9,
            status: "Active"
        },
        {
            id: 4,
            title: "Managing wheat crops during unseasonal rain",
            author: "Suresh Kumar",
            replies: 31,
            status: "Hot Topic"
        }
    ];
    
    // Sample events data
    const eventsData = [
        {
            id: 1,
            title: "Organic Farming Workshop",
            date: "August 15, 2025",
            location: "Delhi Agricultural Center",
            registrationUrl: "#"
        },
        {
            id: 2,
            title: "Modern Irrigation Technologies Expo",
            date: "September 5-7, 2025",
            location: "Hyderabad Convention Center",
            registrationUrl: "#"
        },
        {
            id: 3,
            title: "Annual Farmer's Market & Knowledge Sharing",
            date: "October 12, 2025",
            location: "Punjab Agricultural University",
            registrationUrl: "#"
        }
    ];
    
    // Load forum posts after a brief delay to simulate API call
    setTimeout(() => {
        renderForumPosts();
    }, 1000);
    
    // Load events with a slight additional delay
    setTimeout(() => {
        renderEvents();
    }, 1500);
    
    // Function to render forum posts
    function renderForumPosts() {
        if (!forumPostsContainer) return;
        
        let postsHTML = '';
        
        forumPostsData.forEach(post => {
            let statusClass = '';
            
            switch(post.status.toLowerCase()) {
                case 'active':
                    statusClass = 'status-active';
                    break;
                case 'hot topic':
                    statusClass = 'status-hot';
                    break;
                case 'expert thread':
                    statusClass = 'status-expert';
                    break;
                default:
                    statusClass = '';
            }
            
            postsHTML += `
                <div class="forum-post">
                    <div class="post-header">
                        <h3 class="post-title">${post.title}</h3>
                        <span class="post-status ${statusClass}">${post.status}</span>
                    </div>
                    <p class="post-meta">Started by ${post.author} • ${post.replies} replies</p>
                </div>
            `;
        });
        
        forumPostsContainer.innerHTML = postsHTML;
    }
    
    // Function to render events
    function renderEvents() {
        if (!eventsListContainer) return;
        
        let eventsHTML = '';
        
        eventsData.forEach(event => {
            eventsHTML += `
                <div class="event-item">
                    <h3 class="event-title">${event.title}</h3>
                    <p class="event-details">${event.date} • ${event.location}</p>
                    <a href="${event.registrationUrl}" class="event-register">Register Now</a>
                </div>
            `;
        });
        
        eventsListContainer.innerHTML = eventsHTML;
    }
});